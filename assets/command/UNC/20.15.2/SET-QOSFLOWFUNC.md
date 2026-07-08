---
id: UNC@20.15.2@MMLCommand@SET QOSFLOWFUNC
type: MMLCommand
name: SET QOSFLOWFUNC（设置QoS Flow扩展功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: QOSFLOWFUNC
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话策略管理
- 5GC QoS Flow管理拓展功能
status: active
---

# SET QOSFLOWFUNC（设置QoS Flow扩展功能）

## 功能

**适用NF：SMF**

该命令用于设置QoS Flow相关扩展功能。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| EPSTO5GSQFPLCY | ISMFQFPLCY | DELAYTIMER |
| --- | --- | --- |
| RELEASE | NOT_RELEASE | 60 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EPSTO5GSQFPLCY | EPS切换到5GS专有GBR类型QoS Flow策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定当从EPS切换到5GS携带专有QoS Flow但是没有激活用户面时，专有QoS Flow的处理策略。<br>数据来源：本端规划<br>取值范围：<br>- RELEASE（释放专有QoS Flow）<br>- DELAY_RELEASE（延迟释放专有QoS Flow）<br>- NOT_RELEASE（不释放专有QoS Flow）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST QOSFLOWFUNC查询当前参数配置值。<br>配置原则：无 |
| ISMFQFPLCY | 插入删除I-SMF专有GBR类型QoS Flow策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定当插入I-SMF时，I-SMF获取到的上下文中包含专有GBR类型QoS Flow但是没有激活用户面时专有QoS Flow的处理策略；或者当删除I-SMF时，A-SMF的上下文中包含专有GBR类型QoS Flow但是没有激活用户面时专有QoS Flow的处理策略。<br>数据来源：本端规划<br>取值范围：<br>- RELEASE（释放专有QoS Flow）<br>- DELAY_RELEASE（延迟释放专有QoS Flow）<br>- NOT_RELEASE（不释放专有QoS Flow）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST QOSFLOWFUNC查询当前参数配置值。<br>配置原则：无 |
| DELAYTIMER | 延迟释放专有GBR类型QoS Flow时长(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定专有GBR类型QoS Flow延时释放时长。当ESPTO5GSQFPLCY或者ISMFQFPLCY设置为DELAY_RELASE时，本参数生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~100。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST QOSFLOWFUNC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSFLOWFUNC]] · QoS Flow功能（QOSFLOWFUNC）

## 使用实例

假如运营商需要设置用户EPS切换到5GS时延迟释放专有GBR类型QoS Flow，执行如下命令：

```
SET QOSFLOWFUNC:EPSTO5GSQFPLCY=DELAY_RELEASE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-QOSFLOWFUNC.md`
