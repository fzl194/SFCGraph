---
id: UNC@20.15.2@MMLCommand@LST NRFDRRTSTASW
type: MMLCommand
name: LST NRFDRRTSTASW（查询NRF双活备份状态忽略开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFDRRTSTASW
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF双活容灾参数
status: active
---

# LST NRFDRRTSTASW（查询NRF双活备份状态忽略开关）

## 功能

**适用NF：NRF**

该命令用于查询NRF是否忽略数据备份状态，直接处理业务。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFDRRTSTASW]] · NRF双活备份状态忽略开关（NRFDRRTSTASW）

## 使用实例

查询NRF双活备份状态忽略开关：

```
LST NRFDRRTSTASW:;
%%LST NRFDRRTSTASW:;%%
RETCODE = 0  执行成功

结果如下
-------------------------
双活备份状态忽略开关  =  打开
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF双活备份状态忽略开关（LST-NRFDRRTSTASW）_52070869.md`
