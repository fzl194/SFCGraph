---
id: UNC@20.15.2@MMLCommand@ADD PCFSSCOPE
type: MMLCommand
name: ADD PCFSSCOPE（增加PCF的业务服务区）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PCFSSCOPE
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCF发现和选择管理
- PCF业务服务区
status: active
---

# ADD PCFSSCOPE（增加PCF的业务服务区）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加PCF的业务服务区配置。语音用户通过N7口向PCF请求策略时，可通过服务区名称选择可用PCF。具体过程如下：PCF向NRF注册时携带其服务区名称。会话建立阶段，SMF通过语音用户TAI区域查询配置PCFSSCOPEBIND得到对应的服务区标识，再通过本配置匹配到对应的服务区名称，并携带该服务区名称向NRF查询可用PCF，从而发起会话建立请求。

## 注意事项

- 该命令执行后立即生效。

- 若PCFSSCOPE配置有记录（通过LST PCFSSCOPE查询），且激活请求未携带用户TAI、或根据用户TAI无法从PCFSSCOPEBIND中匹配到合适的SSCOPEID，则从PCFSSCOPE的记录内随机选择一个SSCOPENAME用于PCF服务发现。
- 若PCFSSCOPE配置无记录（通过LST PCFSSCOPE查询），会根据PNFSLCTSSCOPE配置选择SRVSCOPENAME用于PCF服务发现。

- 最多可输入500条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SSCOPEID | 服务区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务区标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。<br>默认值：无<br>配置原则：无 |
| SSCOPENAME | 服务区名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。 区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [PCF的业务服务区（PCFSSCOPE）](configobject/UNC/20.15.2/PCFSSCOPE.md)

## 使用实例

增加PCF的业务服务区，服务区标识为citya，服务区名称为City_A。

```
ADD PCFSSCOPE: SSCOPEID="citya", SSCOPENAME="City_A";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加PCF的业务服务区（ADD-PCFSSCOPE）_35636447.md`
