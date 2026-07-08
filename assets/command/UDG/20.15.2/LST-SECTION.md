---
id: UDG@20.15.2@MMLCommand@LST SECTION
type: MMLCommand
name: LST SECTION（查询地址池IP地址段）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SECTION
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 地址段配置
status: active
---

# LST SECTION（查询地址池IP地址段）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示地址池里的地址段。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定已配置的地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SECTIONNUM | 地址段号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置Section的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SECTION]] · 地址段信息（SECTION）

## 使用实例

- 查询本地地址池pool1中配置的一个地址段，地址池名称为pool1，地址段编号为1：
  ```
  LST SECTION:POOLNAME="pool1",SECTIONNUM=1;
  ```
  ```

  RETCODE = 0  操作成功

  IP地址段信息
  ------------
              地址段号  =  1
            地址池名称  =  pool1
  地址段的起始IPv4地址  =  10.16.86.1
  地址段的终止IPv4地址  =  10.16.87.1
        地址段锁定标志  =  不锁定
      IPv6前缀起始地址  =  ::
            IP地址类型  =  IPV4
      IPv6前缀结束地址  =  ::
          IPv6前缀长度  =  0
                  掩码  =  5
  (结果个数 = 1)

  ---    END
  ```
- 查询本地地址池pool1中配置的所有地址段：
  ```
  LST SECTION: POOLNAME="ipv4pool1";
  ```
  ```

  RETCODE = 0  操作成功。

  IP地址段信息
  ------------
  地址池名称    地址段号    IP地址类型    地址段的起始IPv4地址    地址段的终止IPv4地址    IPv6前缀起始地址    IPv6前缀结束地址    IPv6前缀长度    地址段锁定标志    掩码

  ipv4pool1         0           IPV4          10.1.1.0                10.1.1.200              ::                  ::                  0               不锁定        0
  ipv4pool1         1           IPV4          10.2.1.0                10.2.1.255              ::                  ::                  0               不锁定        0
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SECTION.md`
