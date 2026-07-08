---
id: UNC@20.15.2@MMLCommand@LST SGWPOOL
type: MMLCommand
name: LST SGWPOOL（查询SGW POOL）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGWPOOL
command_category: 查询类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 网络管理
- 业务快速恢复
- SGW Pool
status: active
---

# LST SGWPOOL（查询SGW POOL）

## 功能

**适用NF：PGW-C**

该命令用于显示SGW POOL的信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SGWPOOLNAME | SGW POOL名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGW POOL名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWPOOL]] · SGW POOL（SGWPOOL）

## 使用实例

假设用户需要查询所有的SGW POOL：

```
%%LST SGWPOOL:;%%
RETCODE = 0  操作成功

结果如下
--------
SGW POOL名称  =  sgwpool1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SGWPOOL.md`
