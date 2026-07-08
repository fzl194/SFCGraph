---
id: UNC@20.15.2@MMLCommand@DSP PREFIXFILTERINFO
type: MMLCommand
name: DSP PREFIXFILTERINFO（显示IP前缀列表信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PREFIXFILTERINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 显示路由前缀列表信息
status: active
---

# DSP PREFIXFILTERINFO（显示IP前缀列表信息）

## 功能

该命令用来显示前缀过滤器的基本信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | IP前缀列表名字 | 可选必选说明：可选参数<br>参数含义：该参数用来指定IP前缀列表名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PREFIXFILTERINFO]] · IP前缀列表信息（PREFIXFILTERINFO）

## 使用实例

显示前缀过滤器基本信息：

```
DSP PREFIXFILTERINFO:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
IP前缀列表名字  =  a
        允许数  =  0
        拒绝数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PREFIXFILTERINFO.md`
