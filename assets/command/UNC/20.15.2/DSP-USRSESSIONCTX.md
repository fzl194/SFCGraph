---
id: UNC@20.15.2@MMLCommand@DSP USRSESSIONCTX
type: MMLCommand
name: DSP USRSESSIONCTX（显示指定用户的会话信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: USRSESSIONCTX
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 用户数据库管理
status: active
---

# DSP USRSESSIONCTX（显示指定用户的会话信息）

## 功能

**适用NF：AMF**

显示指定用户的会话信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定国际移动用户标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| PDUSESSIONID | PDU会话标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PDU会话标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRSESSIONCTX]] · 指定用户的会话信息（USRSESSIONCTX）

## 使用实例

显示IMSI为123038000100001用户的会话信息，执行如下命令：

```
%%DSP USRSESSIONCTX:IMSI="123038000100001";%%
RETCODE = 0  操作成功

操作结果如下
------------
PDU会话标识  切片信息  漫游用户归属地切片信息  DNN           RAB状态  EBI ARP映射关系  SM上下文索引  接入类型  归属SMF的Instance ID  拜访SMF的Instance ID  中间SMF的Instance ID  网络切片Instance ID  N11接口的容灾状态  	PDU会话的漫游类型  替换切片信息

5            0-000000  0-000001                huawei.com    否       NULL             1234567890    3GPP接入  smf_instance_10       NULL                  NULL                  NULL                 NotTakeover        	Home Routed        NULL
6            1-111111  2-000011                0168apn1.com  否       NULL             1234567890    3GPP接入  smf_instance_11       NULL                  NULL                  NULL                 PreemptionTakeover  	Home Routed        NULL
7            1-111111  2-000011                0168apn1.com  否       NULL             1234567890    3GPP接入  smf_instance_11       NULL                  NULL                  NULL                 CompleteTakeover		Local Breakout     NULL
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-USRSESSIONCTX.md`
