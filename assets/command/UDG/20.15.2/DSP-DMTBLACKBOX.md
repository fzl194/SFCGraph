---
id: UDG@20.15.2@MMLCommand@DSP DMTBLACKBOX
type: MMLCommand
name: DSP DMTBLACKBOX（显示Diameter黑匣子信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DMTBLACKBOX
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Diameter管理
- 黑匣子信息
status: active
---

# DSP DMTBLACKBOX（显示Diameter黑匣子信息）

## 功能

该命令用于显示Diameter黑匣子信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BOXID | 黑匣子ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定黑匣子ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>当前黑匣子ID：<br>- 链路创建和删除黑匣子，黑匣子ID：1<br>- SOCKET信息，黑匣子ID：2<br>- 服务信息，黑匣子ID：3<br>- 网络消息跟踪信息，黑匣子ID：4<br>- 接口错误信息，黑匣子ID：5<br>- 消息错误信息，黑匣子ID：6<br>- 恢复信息，黑匣子ID：7<br>- 邻居信息，黑匣子ID：8<br>- IPv6信息，黑匣子ID：9<br>- NETCONF信息，黑匣子ID：10<br>- 流控信息，黑匣子ID：11<br>配置原则：无 |
| COMTYPE | 组件类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组件类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RM：路由管理。<br>- CM：连接管理。<br>默认值：无<br>配置原则：无 |
| RUNAME | 资源单元名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“COMTYPE”配置为“CM”时为必选参数。<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DMTBLACKBOX]] · Diameter黑匣子信息（DMTBLACKBOX）

## 使用实例

显示ID为1的Diameter黑匣子信息：

```
DSP DMTBLACKBOX:BOXID=1;
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
  黑匣子ID  =  1
黑匣子信息  = <0000>0828-223625 NotifyNewIncoming:LsConnId[1231] RetCode[6]
<0001>0828-223625 DeleteRMPeerTree:PeerIndex[0x127], PeerAddress[0x245]
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示Diameter黑匣子信息（DSP-DMTBLACKBOX）_00600913.md`
