---
id: UNC@20.15.2@MMLCommand@LST TNFINSIP
type: MMLCommand
name: LST TNFINSIP（查询目标NF实例IP地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TNFINSIP
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 目标NF实例IP地址管理
status: active
---

# LST TNFINSIP（查询目标NF实例IP地址）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询目标NF实例IP地址配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNFINSINDEX | 目标NF实例索引 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF实例索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2047。<br>默认值：无<br>配置原则：<br>本参数需要与ADD TNFINS命令中的TNFINSINDEX值保持一致。 |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPv4）”：IPv4<br>- “IPV6（IPv6）”：IPv6<br>- “NONEIP（无IP）”：无IP<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [目标NF实例IP地址（TNFINSIP）](configobject/UNC/20.15.2/TNFINSIP.md)

## 使用实例

运营商A需要查询索引1的目标NF实例的所有地址信息。

```
%%LST TNFINSIP: TNFINSINDEX=1:;%%
RETCODE = 0  操作成功

结果如下
--------
目标NF实例索引  =  1
    IP地址类型  =  IPv4
  IPV4类型地址  =  10.254.255.10
  IPV6类型地址  =  ::
        端口号  =  60
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询目标NF实例IP地址（LST-TNFINSIP）_09651383.md`
