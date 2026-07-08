---
id: UNC@20.15.2@MMLCommand@LST ALLOWEDPLMN
type: MMLCommand
name: LST ALLOWEDPLMN（查询NF或NF服务支持的PLMN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ALLOWEDPLMN
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 服务支持的PLMN配置管理
status: active
---

# LST ALLOWEDPLMN（查询NF或NF服务支持的PLMN）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于查询NF或NF服务实例支持的PLMN信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NF或NF服务支持的PLMN（ALLOWEDPLMN）](configobject/UNC/20.15.2/ALLOWEDPLMN.md)

## 使用实例

运营商A需要查询所有的PLMN支持信息。

```
%%LST ALLOWEDPLMN:;%%
RETCODE = 0  操作成功

结果如下
--------
    索引标识  =  0
    注册类型  =  RegService
  NF实例名称  =  SMF_Instance_0
服务实例标识  =  Service_Instance_0
移动国家代码  =  460
    移动网号  =  01
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF或NF服务支持的PLMN（LST-ALLOWEDPLMN）_09653265.md`
