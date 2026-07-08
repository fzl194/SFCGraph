---
id: UNC@20.15.2@MMLCommand@LST ROAMINSUPIWL
type: MMLCommand
name: LST ROAMINSUPIWL（查询漫入场景SUPI白名单）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ROAMINSUPIWL
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# LST ROAMINSUPIWL（查询漫入场景SUPI白名单）

## 功能

**适用NF：NRF**

该命令用于查询漫入场景SUPI白名单。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROAMINSUPIWL]] · 漫入场景SUPI白名单（ROAMINSUPIWL）

## 使用实例

查询所有漫入场景SUPI白名单信息：

```
%%LST ROAMINSUPIWL:;%%
RETCODE = 0  操作成功

结果如下
--------
号段起始字符串  =  123456789876501
号段结束字符串  =  123456789876505
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ROAMINSUPIWL.md`
