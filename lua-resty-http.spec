%define lua_dir	%{_datarootdir}/lua
%define lua_dir_resty	%{lua_dir}/5.3/resty

Name: lua-resty-http
Summary: Lua HTTP client cosocket driver for ngx_lua and LuaJIT
Version: 0.16.1
Release: 3
URL: https://github.com/yoannguion/lua-resty-http
License: BSD
Provides: Lua HTTP client cosocket driver for ngx_lua and LuaJIT
BuildArch: noarch

%description
Lua HTTP client cosocket driver for ngx_lua and LuaJIT


%install
mkdir -p $RPM_BUILD_ROOT%{lua_dir_resty}
cp %{_sourcedir}/lib/resty/http.lua $RPM_BUILD_ROOT%{lua_dir_resty}
cp %{_sourcedir}/lib/resty/http_connect.lua $RPM_BUILD_ROOT%{lua_dir_resty}
cp %{_sourcedir}/lib/resty/http_headers.lua $RPM_BUILD_ROOT%{lua_dir_resty}

%files
%{lua_dir_resty}/http.lua
%{lua_dir_resty}/http_connect.lua
%{lua_dir_resty}/http_headers.lua

%changelog
* Mon Aug 01 2022 Yoann GUION <yoann.guion@gmail.com> - 0.16.1-3
- Initial release 0.16.1
