---
id: UNC@20.15.2@MMLCommand@LST SOFTPARAEXP
type: MMLCommand
name: LST SOFTPARAEXP（查询软件参数配置导出模式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SOFTPARAEXP
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
- 操作维护
- 软件参数管理
- 软件参数配置导出
status: active
---

# LST SOFTPARAEXP（查询软件参数配置导出模式）

## 功能

**适用网元：SGSN、MME**

该命令用于查询软件参数配置导出模式，软件参数导出模式是指执行导出命令后，导出的MML配置文件中 [**SET SOFTPARA**](../软件参数/设置软件参数表(SET SOFTPARA)_26146182.md)

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SOFTPARAEXP]] · 软件参数配置导出模式（SOFTPARAEXP）

## 使用实例

查询软件参数配置导出模式：

LST SOFTPARAEXP:;

```
%%LST SOFTPARAEXP:;%%
RETCODE = 0  操作成功。

输出结果如下
------------------------
软件参数导出模式  =  非缺省默认软件参数值
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SOFTPARAEXP.md`
