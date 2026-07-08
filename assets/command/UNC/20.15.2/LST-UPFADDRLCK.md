---
id: UNC@20.15.2@MMLCommand@LST UPFADDRLCK
type: MMLCommand
name: LST UPFADDRLCK（查询锁定的UPF地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPFADDRLCK
command_category: 查询类
applicable_nf:
- SGW-C
- GGSN
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP路径管理
- PFCP路径选择管理
status: active
---

# LST UPFADDRLCK（查询锁定的UPF地址）

## 功能

**适用NF：SGW-C、GGSN、PGW-C、SMF**

该命令用于查询锁定的UPF地址。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPINSTANCEID | UPF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。不区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPFADDRLCK]] · 锁定的UPF地址（UPFADDRLCK）

## 使用实例

查询所有锁定的UPF地址。

```
%%LST UPFADDRLCK:;%%
RETCODE = 0  操作成功。

结果如下
------------------------
   UPF实例标识  =  up1
   UPF的IP版本  =  IPV4
   UPF的IP地址  =  10.0.0.2  
是否开启定时器  =  使能
加锁时长(小时)  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询锁定的UPF地址（LST-UPFADDRLCK）_99602028.md`
