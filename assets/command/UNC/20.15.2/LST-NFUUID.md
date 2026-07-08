---
id: UNC@20.15.2@MMLCommand@LST NFUUID
type: MMLCommand
name: LST NFUUID（查询NF UUID信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFUUID
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
- CBCF
- SPF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF UUID信息管理
status: active
---

# LST NFUUID（查询NF UUID信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBCF、SPF**

该命令用于查询NF实例对应的NF实例标识（UUID）。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFUUID]] · NF UUID信息（NFUUID）

## 使用实例

运营商A需要查询NF实例生成的UUID信息。

```
LST NFUUID:;
%%LST NFUUID:;%%
RETCODE = 0  操作成功

结果如下
------------------------
NF类型   NF实例名称 	   NF实例标识                        

NfNRF    NRF_Instance_0    00000000-0000-0000-0000-000000000013  
NfAMF    AMF_Instance_0    00000000-0000-0000-0000-000000000011  
NfSMF    SMF_Instance_0    00000000-0000-0000-0000-000000000012  
NfNSSF   NSSF_Instance_0   00000000-0000-0000-0000-000000000014  
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFUUID.md`
