---
id: UNC@20.15.2@MMLCommand@ADD NGEMGCNUM
type: MMLCommand
name: ADD NGEMGCNUM（增加紧急号码配置信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NGEMGCNUM
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G 语音业务管理
- 紧急呼叫业务管理
- 紧急呼叫号码配置
status: active
---

# ADD NGEMGCNUM（增加紧急号码配置信息）

## 功能

**适用NF：AMF**

此命令用于配置紧急呼叫号码。系统在给UE发送Registration Accept消息时，会将配置的MCC的紧急呼叫号码携带在消息中发送给UE。

## 注意事项

- 该命令执行后立即生效。

- 紧急呼叫号码必须是运营商已经规划的号码，需要正确配置。配置错误可能导致UE的紧急呼叫接入错误，例如：1.将非紧急呼叫号码配置为紧急呼叫号码，用户被接入至政府部门。2.紧急服务分类配置错误，用户被错误接入其他政府部门。3.当移动国家码与紧急呼叫号码已关联某个非通用的紧急服务类型，如果修改服务类型为“通用类型”需要先删除已有配置后再添加。反之亦然。
- 一个MCC最多能够增加10个紧急呼叫号码。
- 一个MCC下的紧急号码BCD码总长度最大不能超过48字节。
- 是否下发紧急号码列表需要参考SET NGMMFUNC和ADD NGCONNECTPLMN/SET NGEMGSRVFUNC配置说明。

- 最多可输入64条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要配置紧急呼叫号码的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| ESC | 紧急服务分类 | 可选必选说明：必选参数<br>参数含义：该参数用于指定紧急呼叫号码的服务类型。<br>数据来源：全网规划<br>取值范围：<br>- “POLICE（报警）”：报警<br>- “AMBULANCE（医疗救护）”：医疗救护<br>- “FIREBRIGADE（火警）”：火警<br>- “MARINEGUARD（海上救援）”：海上救援<br>- “MOUNTAIN（高山救援）”：高山救援<br>- “ALL（通用类型）”：通用类型<br>默认值：无<br>配置原则：无 |
| NUM | 紧急呼叫号码 | 可选必选说明：必选参数<br>参数含义：该参数用于指明紧急业务对应的号码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~80。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGEMGCNUM]] · 紧急号码配置信息（NGEMGCNUM）

## 使用实例

给移动国家码为“460”的网络增加火警紧急呼叫号码“119”，执行如下命令：

```
ADD NGEMGCNUM: MCC="460", ESC=FIREBRIGADE, NUM="119";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加紧急号码配置信息（ADD-NGEMGCNUM）_09652453.md`
