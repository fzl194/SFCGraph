---
id: UNC@20.15.2@MMLCommand@LOD PACKAGE
type: MMLCommand
name: LOD PACKAGE（加载软件包）
nf: UNC
version: 20.15.2
verb: LOD
object_keyword: PACKAGE
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 升级维护
status: active
---

# LOD PACKAGE（加载软件包）

## 功能

该命令用于加载升级软件包。

## 注意事项

- 该命令执行后立即生效。
- 只有下载新版本后，才能执行该命令加载新版本。
- 如果软件仓中存在该VNFC同版本的软件包，执行[**LOD PACKAGE**](加载软件包（LOD PACKAGE）_59104019.md)命令，加载的是软件仓中的软件包。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPDOBJECT | 升级对象 | 可选必选说明：必选参数<br>参数含义：该参数用于指定升级对象。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BaseSoftware：只升级基础版本。<br>- Patch：只升级补丁。<br>- All：升级基础版本和补丁。<br>默认值：无 |
| BASICPKGVERSIONID | 基础软件包版本号 | 可选必选说明：条件必选参数，该参数在<br>“UPDOBJECT”<br>配置为<br>“BaseSoftware”<br>或<br>“All”<br>时为必选参数。<br>参数含义：该参数用于指定要加载的基础软件包版本号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| PATCHPKGVERSIONID | 补丁版本号 | 可选必选说明：条件必选参数，该参数在<br>“UPDOBJECT”<br>配置为<br>“Patch”<br>或<br>“All”<br>时为必选参数。<br>参数含义：该参数用于指定要加载的补丁版本。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| UPDMODE | 升级模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定升级模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SU：普通升级，一般需要整系统重启。<br>默认值：SU |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PACKAGE]] · 软件包（PACKAGE）

## 使用实例

加载升级软件包：

```
LOD PACKAGE:UPDOBJECT=All,BASICPKGVERSIONID="V100R005C00B021",PATCHPKGVERSIONID="SPH0020"
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LOD-PACKAGE.md`
