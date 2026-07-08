---
id: UNC@20.15.2@MMLCommand@CLR DYNAMICOCS
type: MMLCommand
name: CLR DYNAMICOCS（删除动态OCS）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: DYNAMICOCS
command_category: 动作类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- OCS Diameter连接
- 动态OCS
status: active
---

# CLR DYNAMICOCS（删除动态OCS）

## 功能

**适用NF：PGW-C、SMF**

![](删除动态OCS（CLR DYNAMICOCS）_09896972.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除动态OCS会导致已在线用户无法按照之前的Destination-Host和Destination-Realm封装发送CCR消息。

该命令用于删除动态OCS主机列表表项。

DRA部署场景下，DRA进行OCS寻址，如果寻址到的OCS主机名并未在网关本地配置，则网关会将寻址结果存至动态OCS主机列表。

## 注意事项

- 该命令执行后立即生效。
- 删除动态OCS会导致已在线用户无法按照之前的Destination-Host和Destination-Realm封装发送CCR消息。
- 动态OCS主机列表最多支持2000个表项。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSHOSTNAME | OCS主机名称 | 可选必选说明：可选参数<br>参数含义：主机的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DYNAMICOCS]] · 动态OCS（DYNAMICOCS）

## 使用实例

- 清除指定主机名称的动态OCS信息：
  ```
  CLR DYNAMICOCS:OCSHOSTNAME="ocs-host-name";
  ```
- 清除所有动态OCS信息：
  ```
  CLR DYNAMICOCS:;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-DYNAMICOCS.md`
