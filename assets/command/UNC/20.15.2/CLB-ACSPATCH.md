---
id: UNC@20.15.2@MMLCommand@CLB ACSPATCH
type: MMLCommand
name: CLB ACSPATCH（校正补丁包）
nf: UNC
version: 20.15.2
verb: CLB
object_keyword: ACSPATCH
command_category: 调测类
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

# CLB ACSPATCH（校正补丁包）

## 功能

![](校正补丁包（CLB ACSPATCH）_31115871.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会影响系统的正常运行，请谨慎使用并联系华为支持协助操作。

该命令用于校正补丁包，默认恢复会将补丁恢复到最近一次操作的状态，如果指定补丁版本号，则恢复到指定版本补丁。当补丁删除失败有残留，或者系统存在补丁相关告警时，可以尝试使用该命令进行恢复。

本命令只适用于ACS服务，其他微服务请使用CLB PATCH命令。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后，涉及重启的，需要在重启后参数RBKTIMER所设置的时间内立即登录，并通过DSP PATCHDETAILINFO或者DSP PATCHINFO查询该操作是否成功。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RBTMODE | 重启模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定允许的重启模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：不重启。<br>- SOFT：软重启，不需要重启资源。<br>默认值：NO |
| VERSIONID | 补丁版本号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要恢复的补丁版本号，范围为系统中包含的补丁版本号；如果无此参数，则执行默认恢复。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ACSPATCH]] · 补丁（ACSPATCH）

## 使用实例

校正补丁包：

```
CLB ACSPATCH:VERSIONID="V100R005SPH001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLB-ACSPATCH.md`
