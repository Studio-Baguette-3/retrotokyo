void main()
{
	bool is_therm = false;
	vec4 outC = texture(InputTexture, TexCoord);
	if (outC.r >= 0.99 && outC.g >= 0.99) {
		is_therm = true;
	}

	vec2 coord = TexCoord * 32.0;
	vec2 tc;
	tc.x = coord.x * cos(timer) - coord.y * sin(timer);
	tc.y = coord.x * sin(timer) + coord.y * cos(timer);
	outC = mix(outC, texture(NoiseTexture, tc), 0.3);
	const vec3 W = vec3(0.2125, 0.7154, 0.0721); // luminance in sRGB color space
	float f = dot(outC.rgb, W);
	if (!is_therm) { // make purple if not thermal signature detected
		outC = vec4(f*0.8, f*0.3, f*0.7, 1.0);
	}
	FragColor = outC;
}
