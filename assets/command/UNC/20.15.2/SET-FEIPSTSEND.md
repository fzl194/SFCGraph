---
id: UNC@20.15.2@MMLCommand@SET FEIPSTSEND
type: MMLCommand
name: SET FEIPSTSEND（设置PST广播开关状态）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: FEIPSTSEND
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 设置PST广播开关
status: active
---

# SET FEIPSTSEND（设置PST广播开关状态）

## 功能

![](设置PST广播开关状态（SET FEIPSTSEND）_00840829.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当可能会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

该命令在系统调测的场景，用于设置资源单元PST（Port Status Table）广播开关状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| ISSEND | 发送状态 | 可选必选说明：必选参数<br>参数含义：该参数用于表示开启或关闭PST广播发送状态。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [PST广播开关状态（FEIPSTSEND）](configobject/UNC/20.15.2/FEIPSTSEND.md)

## 使用实例

设置资源单元PST广播开关状态：

```
SET FEIPSTSEND: RUNAME="VNODE_VNRS_VNFC_IPU_0066", ISSEND=FALSE;
RETCODE = 0  操作成功。
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置PST广播开关状态（SET-FEIPSTSEND）_00840829.md`
