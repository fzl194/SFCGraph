---
id: UDG@20.15.2@MMLCommand@LST IPFARMGLOBAL
type: MMLCommand
name: LST IPFARMGLOBAL（查询IPFarm全局参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPFARMGLOBAL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- IP Farm 管理
- IP Farm全局参数
status: active
---

# LST IPFARMGLOBAL（查询IPFarm全局参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示整机针对IP farm配置的负荷分担方式及当前配置的心跳检测功能参数，包括心跳检测成功门限，心跳检测失败门限，心跳检测定时器时长。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVERTYPE | 服务器类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP farm全局配置的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- REDIRECT：指定为重定向。<br>- PCSCF：指定为P-CSCF。<br>- IPMS：指定为IPMS Server。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPFARMGLOBAL]] · IPFarm全局参数（IPFARMGLOBAL）

## 使用实例

查询系统的心跳检测参数和整机针对IP farm配置的负荷分担方式：

```
LST IPFARMGLOBAL:;
```

```

RETCODE = 0  操作成功。

IPFarmGlobal信息
----------------
  时间阈值（秒）  =  10
健康检查成功次数  =  5
健康检查失败次数  =  5
    负载均衡模式  =  最久未被使用
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IPFARMGLOBAL.md`
