---
id: UNC@20.15.2@MMLCommand@LST NFPROFILE
type: MMLCommand
name: LST NFPROFILE（查询NF实例概述信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFPROFILE
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- NCG
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF概述信息管理
status: active
---

# LST NFPROFILE（查询NF实例概述信息）

## 功能

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF**

该命令用于查询配置的NF实例概述信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NF实例概述信息（NFPROFILE）](configobject/UNC/20.15.2/NFPROFILE.md)

## 使用实例

运营商A需要查询所有NF实例概述信息。

```
%%LST NFPROFILE:;%%
RETCODE = 0  操作成功

结果如下
--------
      NF实例名称  =  SMF_Instance_0
          NF类型  =  NfSMF
          NF状态  =  Registered
http地址实例标识  =  2
            域名  =  NULL
      PLMN间域名  =  NULL
            容量  =  100
          优先级  =  0
            负载  =  0
        位置信息  =  NULL
    支持的NF类型  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF实例概述信息（LST-NFPROFILE）_09651589.md`
