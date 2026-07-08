---
id: UNC@20.15.2@MMLCommand@LST GBLOCPORTRGE
type: MMLCommand
name: LST GBLOCPORTRGE（查询本端端口号选择范围）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GBLOCPORTRGE
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
- Gb自动配置管理
- 本端端点端口号管理
status: active
---

# LST GBLOCPORTRGE（查询本端端口号选择范围）

## 功能

**适用网元：SGSN**

此命令用于显示本端端口号选择范围。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GBLOCPORTRGE]] · 本端端口号选择范围（GBLOCPORTRGE）

## 使用实例

显示本端端口号选择范围：

LST GBLOCPORTRGE:;

```
LST GBLOCPORTRGE:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
  起始端口号  =  1024
  结束端口号  =  65535
起始预置端口  =  2000
  预置端口数  =  128
    描述信息  =  DEFAULT
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GBLOCPORTRGE.md`
