---
id: UNC@20.15.2@MMLCommand@ACT PACKAGE
type: MMLCommand
name: ACT PACKAGE（激活软件包）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: PACKAGE
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 升级维护
status: active
---

# ACT PACKAGE（激活软件包）

## 功能

![](激活软件包（ACT PACKAGE）_59103426.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，用于激活升级软件包，若待激活的软件包是基础软件包或冷补丁包，该操作会重启系统，请谨慎使用并联系华为技术支持协助操作。

该命令用于激活升级软件包。

## 注意事项

- 该命令执行后立即生效。
- 只有执行过[**LOD PACKAGE**](加载软件包（LOD PACKAGE）_59104019.md)，才能执行该命令。
- 该命令执行后，涉及重启的，需要在重启后参数RBKTIMER所设置的时间内立即登录，并通过[**DSP UPDVER**](显示当前版本信息（DSP UPDVER）_59103762.md)查询该操作是否成功。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPDOBJECT | 升级对象 | 可选必选说明：必选参数<br>参数含义：该参数用于指定升级对象。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BaseSoftware：只升级基础版本。<br>- Patch：只升级补丁。<br>- All：升级基础版本和补丁。<br>默认值：无 |
| BASICPKGVERSIONID | 基础软件包版本号 | 可选必选说明：条件必选参数，该参数在<br>“UPDOBJECT”<br>配置为<br>“BaseSoftware”<br>或<br>“All”<br>时为必选参数。<br>参数含义：该参数用于指定要加载的基础软件包版本号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| PATCHPKGVERSIONID | 补丁版本号 | 可选必选说明：条件必选参数，该参数在<br>“UPDOBJECT”<br>配置为<br>“Patch”<br>或<br>“All”<br>时为必选参数。<br>参数含义：该参数用于指定要加载的补丁版本。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| RBKTIMER | 回退定时器时长（min） | 可选必选说明：可选参数<br>参数含义：该参数用于指定回退定时器时长，升级后超过该时间不登录客户端，系统将自动回退到升级前版本。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是分钟。<br>默认值：0<br>说明：在容器场景下，该参数只能配置为<br>“0”<br>，表示不支持自动回退。 |
| RBTMODE | 重启模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定允许的重启模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：不重启。<br>- SOFT：软重启，不需要重启资源。<br>默认值：NO<br>说明：在容器场景下，该参数只能配置为NO。 |
| OPERMODE | 操作模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定允许的操作模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>OnlyDBTrans：仅针对高版本配置进行翻译，不备份低版本配置。<br>默认值：无<br>配置原则：无。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [软件包（PACKAGE）](configobject/UNC/20.15.2/PACKAGE.md)

## 使用实例

激活升级软件包：

```
ACT PACKAGE:UPDOBJECT=All,BASICPKGVERSIONID="V100R005C00B021",PATCHPKGVERSIONID="SPH0020",RBKTIMER=10,RBTMODE=SOFT,OPERMODE=OnlyDBTrans
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/激活软件包（ACT-PACKAGE）_59103426.md`
