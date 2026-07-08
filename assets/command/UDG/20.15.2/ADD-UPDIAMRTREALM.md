---
id: UDG@20.15.2@MMLCommand@ADD UPDIAMRTREALM
type: MMLCommand
name: ADD UPDIAMRTREALM（增加Diameter路由域名信息）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPDIAMRTREALM
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 256
category_path:
- 用户面服务管理
- Diameter管理
- 路由管理
- Diameter路由
status: active
---

# ADD UPDIAMRTREALM（增加Diameter路由域名信息）

## 功能

**适用NF：UPF**

此命令用于添加指定Diameter应用和realm的Diameter路由相关参数，或者设置指定Diameter应用的缺省Diameter路由的相关参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为256。
- 该命令Failover和自动倒回相关的功能当前版本暂不支持。
- 应用和realm唯一确定一条记录。
- 主备路由选择模式下，如果主用下一跳被删除，则第一个备用下一跳升主。
- 网关发送的请求消息中携带的Destination-Realm AVP值用于Realm路由表匹配，根据消息的应用类型以及Destination-Realm AVP值匹配到Diameter路由时，UPF按照select-mode设置选择下一跳。如无法匹配到某Diameter应用所有指定的路由，同时该应用配置了缺省路由，该请求消息按照缺省路由发送。
- 基于会话轮循的路由选择模式下，根据Session-id选择的DRA状态异常时，会选择Diameter路由中下一个链路正常的DRA进行消息交互。当根据Session-id选择的DRA状态恢复正常后，会重新选择该DRA进行消息交互。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALMNAME | Diameter域名名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的realm名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 2670控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| APPLICATION | Diameter应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：无 |
| SELECTMODE | 路由选择模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定到同一realm的多条路由的路由选择模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER_SLAVE：主备模式。<br>- SESSION_ID：基于会话的轮循模式。<br>- ROUND_ROBIN：基于消息的轮循模式。<br>默认值：SESSION_ID<br>配置原则：无 |
| FAILOVERSW | Failover开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的Failover开关是否开启。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：DISABLE<br>配置原则：无 |
| AUTOFAILBACKSW | 自动倒回开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的自动倒回开关是否开启。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：DISABLE<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMRTREALM]] · Diameter路由域名信息（UPDIAMRTREALM）

## 使用实例

- 添加一个Swm接口的缺省Diameter路由参数，路由选择模式为基于会话的轮循（session-id）：
  ```
  ADD UPDIAMRTREALM: REALMNAME="default", APPLICATION=SWM,SELECTMODE=SESSION_ID;
  ```
- 添加一个指定realm名为example.com的Swm应用的Diameter路由参数，模式为主备，支持failover处理，支持主动failback到主用下一跳：
  ```
  ADD UPDIAMRTREALM: REALMNAME="example.com", APPLICATION=SWM, SELECTMODE=MASTER_SLAVE, FAILOVERSW=ENABLE, AUTOFAILBACKSW=ENABLE;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加Diameter路由域名信息（ADD-UPDIAMRTREALM）_97080169.md`
