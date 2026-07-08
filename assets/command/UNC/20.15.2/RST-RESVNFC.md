---
id: UNC@20.15.2@MMLCommand@RST RESVNFC
type: MMLCommand
name: RST RESVNFC（复位VNFC）
nf: UNC
version: 20.15.2
verb: RST
object_keyword: RESVNFC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 操作维护
- 配置管理
- 复位网元信息
status: active
---

# RST RESVNFC（复位VNFC）

## 功能

![](复位VNFC（RST RESVNFC）_51149357.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，该命令会重启VNFP或指定的VNFC。如果是强制重启，还可能会导致正在操作的配置丢失，请谨慎使用并联系华为技术支持协助操作。

该命令用于重启VNFP或指定VNFC。

当VNFC出现系统异常时，可使用本命令进行恢复。

## 注意事项

- 该命令执行后立即生效。
- 本命令属于高危命令，操作不当会导致业务故障。
- 在VNFP上运行该命令后，当复位VNFP时，会复位已注册的虚拟节点。当复位指定VNFC时，父资源节点已注册的虚拟节点支持复位，父资源节点未注册的虚拟节点不支持复位。
- 虚拟节点复位时，自动保存配置信息；复位期间，虚拟节点承载的业务会中断；复位后，虚拟节点恢复到正常状态。
- 对于多次使用该命令且指定ISFORCEOPER参数为“FALSE”或者不输入该参数重启系统，一直提示“系统正忙，请稍后重试。”的场景下，如果确认系统发生故障需要强制重启，则可以通过指定ISFORCEOPER参数为“TRUE”，强制重启系统。但是，强制重启系统时，可能会导致部分配置因为未提交成功而丢失，建议谨慎操作。
- 该命令仅支持在虚拟机场景下复位指定VNFC，不支持在容器场景下复位指定VNFC。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNFCNAME | VNFC实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VNFP或VNFC实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| ISFORCEOPER | 强制操作标志 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否强制重启。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：<br>**FALSE** |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RESVNFC]] · 复位VNFC（RESVNFC）

## 使用实例

- 复位VNFP：
  ```
  RST RESVNFC:VNFCNAME="VNFP", ISFORCEOPER=FALSE;
  ```
- 复位指定的VNFC：
  ```
  RST RESVNFC:VNFCNAME="kk", ISFORCEOPER=FALSE;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RST-RESVNFC.md`
