---
id: UNC@20.15.2@MMLCommand@LST TAIRANGELIST
type: MMLCommand
name: LST TAIRANGELIST（查询NF TAI区域信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TAIRANGELIST
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
- NF TAI区域信息管理
status: active
---

# LST TAIRANGELIST（查询NF TAI区域信息）

## 功能

**适用NF：AMF、SMF、NSSF、NRF、SMSF、NCG**

该命令用于查询NF实例支持的TAI区域信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NF TAI区域信息（TAIRANGELIST）](configobject/UNC/20.15.2/TAIRANGELIST.md)

## 使用实例

运营商A需要查询所有NF实例支持的TAI区域信息。

```
%%LST TAIRANGELIST:;%%
RETCODE = 0  操作成功

结果如下
--------
        NF实例名称  =  SMF_Instance_0
            NF类型  =  NfSMF
      移动国家代码  =  460
          移动网号  =  01
       TAC区域标识  =  0
  绑定的SMFINFO ID  =  null
绑定的NWDAFINFO ID  =  null
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF-TAI区域信息（LST-TAIRANGELIST）_09653101.md`
