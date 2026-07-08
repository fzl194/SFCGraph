---
id: UNC@20.15.2@MMLCommand@LST CACHESPECS
type: MMLCommand
name: LST CACHESPECS（查询缓存数据规格）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CACHESPECS
command_category: 查询类
applicable_nf:
- AMF
- SMF
- SMSF
- NCG
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF Cache管理
status: active
---

# LST CACHESPECS（查询缓存数据规格）

## 功能

**适用NF：AMF、SMF、SMSF、NCG、NSSF**

该命令用于查询从NRF中获得的远端NF信息缓存数据规格。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [缓存数据规格（CACHESPECS）](configobject/UNC/20.15.2/CACHESPECS.md)

## 使用实例

运营商A需要查询从NRF中获得的远端NF信息缓存数据规格：

```
%%LST CACHESPECS:;%%
RETCODE = 0  操作成功

结果如下
------------------------
           网元缓存规格  =  4000                    
     SUPI及GPSI缓存规格  =  4000000
       TAIRANGE缓存规格  =  1500000
            DNN缓存规格  =  3000000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询缓存数据规格（LST-CACHESPECS）_62337370.md`
