// It can be used on any file because is global.
int g_variable = 5;

// It will be used just in this file.
static int s_variable = 10;

// We have another function on the main, however,
// Doesn't will be problems with our two functions
// called equals (function).
static void function()
{
    // stuff
}