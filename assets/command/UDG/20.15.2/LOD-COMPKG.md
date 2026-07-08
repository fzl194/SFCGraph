---
id: UDG@20.15.2@MMLCommand@LOD COMPKG
type: MMLCommand
name: LOD COMPKG（加载扩展包）
nf: UDG
version: 20.15.2
verb: LOD
object_keyword: COMPKG
command_category: 动作类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 操作维护
- 网元管理
status: active
---

# LOD COMPKG（加载扩展包）

## 功能

![](加载扩展包（LOD COMPKG）_42742473.assets/notice_3.0-zh-cn.png)

- 此命令为高危命令，请谨慎使用并联系华为技术支持协助操作。
- 部署了CGPLite服务的系统，如果涉及组件包的加载，组件包加载成功后CGPLite服务会自动重启，正常情况下复位需要一分钟左右的时间，重启期间CGPLite相关业务不可用。

网元采用扩容方式上线扩展域业务，需要执行此命令完成扩展域适配包、组件包的加载。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：无。 |
| PKGNAME | 网元包名称 | 可选必选说明：可选参数。<br>参数含义：上线扩展域网元业务时所需的网元包名称，网元包中包含扩展域适配包、组件包。通过VNFM上传后，该网元包将存储在VNFM系统后台，路径如下：/export/home/catalog/softpkg/HUAWEI/{APPTYPE}/{VERSION}/{PKGNAME}。<br>取值范围：长度不超过50的字符串。<br>默认值：无。<br>配置原则：网元包名称和适配包名称不能同时为空。 |
| PATCHPKGNAME | 网元补丁包名称 | 可选必选说明：可选参数。<br>参数含义：基于补丁版本上线扩展域网元业务时所需的网元补丁包名称，网元补丁包中包含扩展域适配包、组件包。通过VNFM上传后，该网元包将存储在VNFM系统后台，路径如下：/export/home/catalog/softpkg/HUAWEI/{APPTYPE}/{PATCHVERSION}/{PATCHPKGNAME}。<br>取值范围：长度不超过50的字符串。<br>默认值：无。<br>配置原则：输入网元补丁包名称时必须输入网元包名称。 |
| OMANAME | 适配包名称 | 可选必选说明：可选参数。<br>参数含义：上线扩展域网元业务时所需的适配包名称。适配包中包含扩展域的适配包，通过VNFM上传后，该适配包将存储在VNFM系统后台，路径如下：<br>/export/home/catalog/softpkg/HUAWEI/{APPTYPE}/{VERSION}/{OMANAME}。<br>取值范围：长度不超过50的字符串。<br>默认值：无。<br>配置原则：<br>- 网元包名称和适配包名称不能同时为空。<br>- 对于软件包解耦场景，扩展域组件包和扩展域适配包不在同一个大包下，需要将扩展域组件包所在的软件包名称输入到网元包名称参数中，扩展域适配包所在的软件包的包名称输入到适配包名称中。<br>- 对于上线的扩展域只有适配包需要加载场景，只用输入适配包名称即可。 |
| PATCHOMANAME | 补丁适配包名称 | 可选必选说明：可选参数。网元包名称和适配包名称不能同时为空<br>参数含义：基于补丁版本上线扩展域网元业务时所需的补丁适配包名称，补丁适配包中包含扩展域适配包。通过VNFM上传后，该补丁适配包将存储在VNFM系统后台，路径如下：/export/home/catalog/softpkg/HUAWEI/{APPTYPE}/{PATCHVERSION}/{PATCHOMANAME}。<br>取值范围：长度不超过50的字符串。<br>默认值：无。<br>配置原则：输入补丁适配包名称时必须输入适配包名称。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@COMPKG]] · 扩展包（COMPKG）

## 使用实例

加载网元ID为219，网元包名称为APP_20.X的软件包。

```
%%LOD COMPKG: MEID=219, PKGNAME="APP_20.X";%%
RETCODE = 0  正在下载适配包

进度报告
--------
已完成 = 20%
(结果个数 = 1)

---    END

%%LOD COMPKG: MEID=219, PKGNAME="APP_20.X";%%
RETCODE = 0  正在推送适配包

进度报告
--------
已完成 = 50%
(结果个数 = 1)

---    END

%%LOD COMPKG: MEID=219, PKGNAME="APP_20.X";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LOD-COMPKG.md`
