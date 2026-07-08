---
id: UNC@20.15.2@MMLCommand@LST NFSERVICEVER
type: MMLCommand
name: LST NFSERVICEVER（查询NF服务版本信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFSERVICEVER
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF服务版本管理
status: active
---

# LST NFSERVICEVER（查询NF服务版本信息）

## 功能

**适用NF：AMF、SMF、NSSF、NRF、SMSF、NCG**

该命令用于查询NF服务实例的版本信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NFS实例所归属的NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |
| SRVINSTANCEID | 服务实例标识 | 可选必选说明：可选参数<br>参数含义：本参数用于指定NFS实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数与ADD NFSERVICE命令中的SRVINSTANCEID值一致时生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFSERVICEVER]] · NF服务版本信息（NFSERVICEVER）

## 使用实例

运营商A需要查询所有服务实例的版本信息。

```
%%LST NFSERVICEVER:;%%
RETCODE = 0  操作成功

结果如下
--------
  NF实例名称  =  AMF_Instance_0
服务实例标识  =  Service_Instance_0
 API版本信息  =  1.0.0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFSERVICEVER.md`
