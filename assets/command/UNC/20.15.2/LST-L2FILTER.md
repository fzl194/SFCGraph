---
id: UNC@20.15.2@MMLCommand@LST L2FILTER
type: MMLCommand
name: LST L2FILTER（查询层二过滤器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: L2FILTER
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 层二过滤器
status: active
---

# LST L2FILTER（查询层二过滤器）

## 功能

**适用NF：SMF**

该命令用于查询层二过滤器。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILTERNAME | 层二过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定层二过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/L2FILTER]] · 层二过滤器（L2FILTER）

## 使用实例

- 查询所有的层二过滤器：
  ```
  LST L2FILTER: FILTERNAME="filter1";
  RETCODE = 0  操作成功

  结果如下
  --------
    过滤器名称  =  filter1
     源MAC地址  =  00E0-FC12-3456
   目的MAC地址  =  00E0-FC12-3457
    VLAN标识符  =  1
  优先级编码点  =  1
    丢弃指示器  =  ENABLE
      以太类型  =  PROFINET
  (结果个数 = 1)

  ---    END
  ```
- 查询层二过滤器名称为“filter1”的层二过滤器：
  ```
  LST L2FILTER:;
  RETCODE = 0  操作成功

  结果如下
  --------
    过滤器名称  =  filter1
     源MAC地址  =  00E0-FC12-3456
   目的MAC地址  =  00E0-FC12-3457
    VLAN标识符  =  1
  优先级编码点  =  1
    丢弃指示器  =  ENABLE
      以太类型  =  PROFINET
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-L2FILTER.md`
