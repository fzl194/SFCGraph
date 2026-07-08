---
id: UNC@20.15.2@MMLCommand@DSP PACKAGE
type: MMLCommand
name: DSP PACKAGE（显示系统软件信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PACKAGE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 版本信息
status: active
---

# DSP PACKAGE（显示系统软件信息）

## 功能

该命令用于显示系统软件包的信息，如软件包类型、版本号和运行状态等。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PACKAGETYPE | 包类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示包类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Version：软件版本包，包括基础版本包、冷补丁、热补丁等几种。<br>- RiskCheckPackage：风险排查包。<br>- AppPackage：App软件包。<br>默认值：无 |
| VERSIONTYPE | 版本类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示版本类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BaseSoftware：包含网元或APP运行所需所有软件的全版本。<br>- ColdPatch：为网元或APP运行所需的部分软件，为对基础版本的补充，冷补丁不能独立运行，冷补丁升级可能会中断业务。<br>- HotPatch：为对基础版本或冷补丁的热补充，热补丁不能独立运行，热补丁升级不中断业务。<br>默认值：无 |
| VERSIONID | 版本号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示版本号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| APPTYPE | 版本应用类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示版本应用类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| VERSIONSTATUS | 版本状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示版本状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Ready：软件包已准备好，可用。<br>- Prepared：软件包处于加载状态。<br>- Running：软件包处于运行状态。<br>- RunningAndPrepared：软件包处于运行和已加载状态。<br>默认值：无 |
| CPUARCHTYPE | CPU架构类型 | 可选必选说明：可选参数<br>参数含义：CPU架构类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- X86：CPU架构类型是X86。<br>- ARM：CPU架构类型是ARM。<br>- Any：不区分CPU架构类型。<br>默认值：无 |
| BASEVERSIONID | 基础版本号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示基础版本号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PACKAGE]] · 软件包（PACKAGE）

## 使用实例

显示系统软件包：

```
DSP PACKAGE:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-----------
包类型           版本类型         版本号                   版本应用类型             版本状态           CPU架构类型           基础版本号
版本包           基础版本         V100R018C20B270          BaseApp                  运行               X86                   V100R018C20B270
版本包           基础版本         V100R018C20              GuestOS                  运行&已加载        X86                   V100R018C20B270
风险排查包       基础版本         V100R018C20CHK           BaseApp                  可用               X86                   V100R018C20B270
App软件包        热补丁           V100R018C20B050          PAEDP                    已加载             X86                   V100R018C20B270
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示系统软件信息（DSP-PACKAGE）_59103342.md`
