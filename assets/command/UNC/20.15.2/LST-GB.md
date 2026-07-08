---
id: UNC@20.15.2@MMLCommand@LST GB
type: MMLCommand
name: LST GB（查询Gb通用信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GB
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb通用信息参数
status: active
---

# LST GB（查询Gb通用信息）

## 功能

**适用网元：SGSN**

该命令用于查询GB通用信息。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/GB]] · Gb通用信息（GB）

## 使用实例

查询GB通用参数:

LST GB:;

```
%%LST GB:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
    启用Gb over IP资源分配功能  =  是
启用Gb动态 over IP自动配置功能  =  否
  启用Gb over IP接口UDP校验功能 =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Gb通用信息(LST-GB)_26305816.md`
