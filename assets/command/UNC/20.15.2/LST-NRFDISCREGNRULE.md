---
id: UNC@20.15.2@MMLCommand@LST NRFDISCREGNRULE
type: MMLCommand
name: LST NRFDISCREGNRULE（查询服务发现区域识别规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFDISCREGNRULE
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF服务发现区域识别规则配置管理
status: active
---

# LST NRFDISCREGNRULE（查询服务发现区域识别规则）

## 功能

**适用NF：NRF**

该命令用于查询NRF服务发现区域识别规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFDISCREGNRULE]] · 服务发现区域识别规则（NRFDISCREGNRULE）

## 使用实例

查询NRF服务发现区域识别规则。

```
LST NRFDISCREGNRULE:;
%%LST NRFDISCREGNRULE:;%%
RETCODE = 0  操作成功

结果如下
--------
            网元类型  =  CUSTOM_OCS
区域关系精确匹配开关  =  打开
    区域信息起始位置  =  3
        区域信息长度  =  8
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询服务发现区域识别规则（LST-NRFDISCREGNRULE）_71436539.md`
