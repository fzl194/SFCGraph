---
id: UDG@20.15.2@MMLCommand@LST IPOPTSECURITY
type: MMLCommand
name: LST IPOPTSECURITY（查询IP选项安全配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPOPTSECURITY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- IP选项安全配置
status: active
---

# LST IPOPTSECURITY（查询IP选项安全配置）

## 功能

该命令用于查询IP选项安全配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTIONTYPE | IP选项类型 | 可选必选说明：可选参数<br>参数含义：该参数表示IP选项的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- routeAlert：系统处理带路由告警选项IP报文的功能。<br>- routeRecord：系统处理带记录路由选项IP报文的功能。<br>- sourceRoute：系统处理带源路由选项IP报文的功能。该选项控制报文传输路径。<br>- timeStamp：系统处理带记录时间戳选项IP报文的功能。该选项用于计算报文传输/处理时消耗的时间。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPOPTSECURITY]] · IP选项安全配置（IPOPTSECURITY）

## 使用实例

查询记录路由选项routeRecord的配置实例：

```
LST IPOPTSECURITY: OPTIONTYPE=routeRecord;
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
            IP选项类型  =  路由记录选项
        IP选项配置开关  =  使能
        (结果个数 = 1)
        ---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IP选项安全配置（LST-IPOPTSECURITY）_00440645.md`
