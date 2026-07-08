---
id: UDG@20.15.2@MMLCommand@SET GLBDLLTBUFFER
type: MMLCommand
name: SET GLBDLLTBUFFER（设置全局下行数据长时间缓存个数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLBDLLTBUFFER
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- GTP隧道管理
- 全局下行数据长时间缓存
status: active
---

# SET GLBDLLTBUFFER（设置全局下行数据长时间缓存个数）

## 功能

**适用NF：UPF**

此命令用来配置全局的用户下行数据长时间缓存时的最大缓存个数及存储方式。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 该命令仅在不配置APN场景下生效。
- 如果UPF配置的下行数据缓存个数超过Serving PLMN速率控制的Downlink Rate Limit值，则当缓存的包数超过Downlink Rate Limit时会触发丢包。 所以，设置下行数据缓存个数时需要同时考虑无线侧的能力，下行缓存个数设置过大超过无线的处理能力可能引发丢包。
- 该命令在下行缓存时长超过15秒时生效，下行缓存时长小于15秒时，默认下行缓存报文数量为128个。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | MAXBUFFERNUM | BUFFERMODE |
| --- | --- | --- |
| 初始值 | 1 | BUFF_MODE_RING |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MAXBUFFERNUM | 最大缓存个数 | 可选必选说明：必选参数<br>参数含义：该参数用于设置全局级的下行数据长时间缓存时的最大缓存个数。当获取了License控制项为“82200CKC LKV3G5NDRX01 NB-IoT eDRX模式”或者“82200FYD LKV3G5EDRX01 5G eDRX模式”的license时，该参数与session modification request/session report response消息携带的缓存个数取最小值作为系统实际缓存的最大个数; 否则，使用参数配置作为系统实际缓存的最大个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～64，单位是包数。<br>默认值：无<br>配置原则：无 |
| BUFFERMODE | 存储方式 | 可选必选说明：必选参数<br>参数含义：该参数用于设置缓存报文达到规格时，报文的存储方式。环形存储是指丢弃最先存储的报文，缓存当前报文；链式存储是指丢弃当前收到的报文。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BUFF_MODE_RING：环形存储。<br>- BUFF_MODE_CHAIN：链式存储。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [全局下行数据长时间缓存配置（GLBDLLTBUFFER）](configobject/UDG/20.15.2/GLBDLLTBUFFER.md)

## 关联任务

- [0-00173](task/UDG/20.15.2/0-00173.md)

## 使用实例

配置全局下行报文长时间缓存得最大个数为64个，存储方式为环形存储：

```
SET GLBDLLTBUFFER: MAXBUFFERNUM=64, BUFFERMODE=BUFF_MODE_RING;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置全局下行数据长时间缓存个数（SET-GLBDLLTBUFFER）_86530268.md`
