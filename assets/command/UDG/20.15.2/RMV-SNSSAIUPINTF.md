---
id: UDG@20.15.2@MMLCommand@RMV SNSSAIUPINTF
type: MMLCommand
name: RMV SNSSAIUPINTF（删除网络切片和逻辑接口绑定关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SNSSAIUPINTF
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- 网络切片管理
- 网络切片与逻辑接口绑定关系配置
status: active
---

# RMV SNSSAIUPINTF（删除网络切片和逻辑接口绑定关系）

## 功能

**适用NF：UPF**

![](删除网络切片和逻辑接口绑定关系（RMV SNSSAIUPINTF）_51061267.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行该命令会导致切片用户使用的逻辑接口发生变化，可能会导致业务链路不通。不携带参数执行命令时会删除所有切片和逻辑接口的绑定。

该命令用于删除指定的网络切片选择标识绑定的N3逻辑接口信息。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 支持不带参数，或者只指定SST，或者指定SST和SD删除配置。不允许只指定SD删除配置。如果不指定SD，删除的是指定SST，SD为"ffffff"的逻辑接口绑定配置。
- 不携带参数执行命令时会删除所有切片和逻辑接口的绑定，请谨慎操作。
- 删除指定切片和逻辑接口的绑定关系会导致切片用户选择的逻辑接口发生变化，可能会导致业务链路不通。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SST | 切片/服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用来设置切片/服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无<br>配置原则：无 |
| SD | 切片区分码 | 可选必选说明：可选参数<br>参数含义：该参数用来指定切片区分码。<br>数据来源：全网规划<br>取值范围：字符串类型，每个字符必须为0~9的数字或a~f/A-F的字母。<br>默认值：无<br>配置原则：该参数必须是长度为6的字符串。如果S-NSSAI无SD，需配置为全F。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SNSSAIUPINTF]] · 网络切片和逻辑接口绑定关系（SNSSAIUPINTF）

## 使用实例

- 删除SST为1，SD为“123456”的SNSSAIUPINTF配置信息：
  ```
  RMV SNSSAIUPINTF: SST=1, SD="123456";
  ```
- 删除SST为1，SD为"ffffff"的SNSSAIUPINTF配置信息：
  ```
  RMV SNSSAIUPINTF: SST=1;
  ```
- 删除UPF配置的所有SNSSAIUPINTF配置信息：
  ```
  RMV SNSSAIUPINTF:;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-SNSSAIUPINTF.md`
