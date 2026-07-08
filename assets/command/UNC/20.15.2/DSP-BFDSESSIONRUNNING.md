---
id: UNC@20.15.2@MMLCommand@DSP BFDSESSIONRUNNING
type: MMLCommand
name: DSP BFDSESSIONRUNNING（查询BFD会话的运行信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BFDSESSIONRUNNING
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- BFD维护
status: active
---

# DSP BFDSESSIONRUNNING（查询BFD会话的运行信息）

## 功能

该命令用于查询BFD会话的运行信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALDISCR | 本地标识符 | 可选必选说明：必选参数<br>参数含义：本地描述符。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～49152。<br>默认值：无 |

## 操作的配置对象

- [BFD会话的运行信息（BFDSESSIONRUNNING）](configobject/UNC/20.15.2/BFDSESSIONRUNNING.md)

## 使用实例

查询BFD会话的运行信息：

```
DSP BFDSESSIONRUNNING:LOCALDISCR=1;
```

```

RETCODE = 0  操作成功。

结果如下
----------------
           本地标识符  =  1
             会话状态  =  DOWN
           本地诊断字  =  无
         会话Down原因  =  无

(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BFD会话的运行信息（DSP-BFDSESSIONRUNNING）_49802122.md`
