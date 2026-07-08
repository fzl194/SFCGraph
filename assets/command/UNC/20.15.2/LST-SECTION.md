---
id: UNC@20.15.2@MMLCommand@LST SECTION
type: MMLCommand
name: LST SECTION（查询地址段）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SECTION
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址段管理
status: active
---

# LST SECTION（查询地址段）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询SMF上为激活本地分配地址的用户创建的地址段。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定已配置的地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |
| SECTIONNUM | 地址段号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置Section的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECTION]] · 地址段（SECTION）

## 使用实例

查询地址池名为pool2,地址段号为2的地址段信息: LST SECTION: POOLNAME="pool2", SECTIONNUM=2;

```
%%LST SECTION: POOLNAME="pool2", SECTIONNUM=2;%%
RETCODE = 0  操作成功。

结果如下
-------------------------
       地址池名称  =  pool2
         地址段号  =  2
       IP地址类型  =  IPv6
     IPv4开始地址  =  0.0.0.0
     IPv4结束地址  =  0.0.0.0
     IPv4地址个数  =  0
 IPv6前缀起始地址  =  2001:DB8::
 IPv6前缀结束地址  =  2001:DB8:0:10::
     IPv6前缀长度  =  64
     IPv6地址个数  =  17
   地址段锁定标志  =  解锁
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SECTION.md`
