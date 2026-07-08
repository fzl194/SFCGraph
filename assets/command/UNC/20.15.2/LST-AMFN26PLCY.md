---
id: UNC@20.15.2@MMLCommand@LST AMFN26PLCY
type: MMLCommand
name: LST AMFN26PLCY（查询AMF N26接口策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFN26PLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- N26接口管理
- N26策略管理
status: active
---

# LST AMFN26PLCY（查询AMF N26接口策略）

## 功能

**适用NF：AMF**

该命令用于查询AMF的N26接口部署策略相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFN26PLCY]] · AMF N26接口策略（AMFN26PLCY）

## 使用实例

查询AMF的N26接口部署策略，执行如下命令：

```
%%LST AMFN26PLCY:;%%
RETCODE = 0  操作成功

结果如下
--------
        AMF N26接口部署方式  =  N26接口独立部署
      是否支持UAM内部互操作  =  否
          UAM内切换识别模式  =  通过DNS查询结果识别
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFN26PLCY.md`
