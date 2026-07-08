---
id: UNC@20.15.2@MMLCommand@LST VLROFFLOADINF
type: MMLCommand
name: LST VLROFFLOADINF（查询VLR迁移配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VLROFFLOADINF
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- MSC POOL管理
- VLR迁移配置信息
status: active
---

# LST VLROFFLOADINF（查询VLR迁移配置信息）

## 功能

**适用网元：SGSN、MME**

该命令用来查询与本局 UNC 相连的MSC POOL中VLR的迁移配置信息。

## 注意事项

第二阶段迁移速度为每个SPP进程上每秒迁移的最大用户数。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLROFFLOADINF]] · VLR迁移配置信息（VLROFFLOADINF）

## 使用实例

查询迁移配置信息：

LST VLROFFLOADINF:;

```
%%LST VLROFFLOADINF:;%%
RETCODE = 0  操作成功。

输出结果如下
---------
 第一阶段迁移时长(分钟) = 40   
第二阶段迁移速度(个/秒) = 30
      

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VLROFFLOADINF.md`
