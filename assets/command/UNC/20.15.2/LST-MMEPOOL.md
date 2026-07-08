---
id: UNC@20.15.2@MMLCommand@LST MMEPOOL
type: MMLCommand
name: LST MMEPOOL（查询MME POOL）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MMEPOOL
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 网络管理
- 业务快速恢复
- MME Pool
status: active
---

# LST MMEPOOL（查询MME POOL）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于查询MME POOL。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEPOOLNAME | MME POOL名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME POOL名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMEPOOL]] · MME POOL（MMEPOOL）

## 使用实例

假设用户需要查询所有的MME POOL：

```
%%LST MMEPOOL:;%%
RETCODE = 0  操作成功

结果如下
--------
       MME POOL名称  =  mmepool1
       SGW POOL名称  =  NULL
指定备份MME功能开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MME-POOL（LST-MMEPOOL）_31453516.md`
