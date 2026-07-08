---
id: UNC@20.15.2@MMLCommand@LST LOWPRIDSCP
type: MMLCommand
name: LST LOWPRIDSCP（查询低优先级业务DSCP）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOWPRIDSCP
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 低优先级DSCP
status: active
---

# LST LOWPRIDSCP（查询低优先级业务DSCP）

## 功能

**适用网元：SGSN**

该命令用于查询低优先级业务与DSCP的对应关系。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOWPRIDSCP]] · 低优先级业务DSCP（LOWPRIDSCP）

## 使用实例

查询低优先级业务的DSCP配置：

LST LOWPRIDSCP:;

```
%%LST LOWPRIDSCP:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
 DSCP起始值  DSCP结束值

 0           5       
 6           11      
 14          25      
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询低优先级业务DSCP(LST-LOWPRIDSCP)_26305322.md`
