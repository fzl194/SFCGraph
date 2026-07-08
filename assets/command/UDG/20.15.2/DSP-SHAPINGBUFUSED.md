---
id: UDG@20.15.2@MMLCommand@DSP SHAPINGBUFUSED
type: MMLCommand
name: DSP SHAPINGBUFUSED（查询整形使用的缓存）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SHAPINGBUFUSED
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 流量管理
- 整形缓存使用率
status: active
---

# DSP SHAPINGBUFUSED（查询整形使用的缓存）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查看整形缓存的使用情况。

## 注意事项

- 该命令执行后立即生效。
- 如果输入的POD名称为空，则查所有POD的整形缓存使用情况。
- 如果输入的POD名称不为空，则查指定POD的整形缓存使用情况。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SHAPINGBUFUSED]] · 整形使用的缓存（SHAPINGBUFUSED）

## 使用实例

- 查询所有POD的整形缓存使用情况：
  ```
  DSP SHAPINGBUFUSED:;
  ```
  ```

  RETCODE = 0 操作成功。

  整形缓存使用信息
  --------
  POD名称                使用的缓存数  总缓存数  IPSQM使用的缓存数  IPSQM总缓存数

  isu-pod-0178-32-2-101  0             200032    0                  85128
  isu-pod-2178-32-2-121  0             200032    0                  85128
  (结果个数 = 2)
  --- END
  ```
- 查询名称为“isu-pod-0178-32-2-101”的POD的整形缓存使用情况：
  ```
  DSP SHAPINGBUFUSED:PODNAME="isu-pod-0178-32-2-101";
  ```
  ```

  RETCODE = 0 操作成功。

  整形缓存使用信息
  -------------------------
  POD名称            =  isu-pod-0178-32-2-101
  使用的缓存数       =  0
  总缓存数           =  20032
  IPSQM使用的缓存数  =  0
  IPSQM总缓存数      =  85128
  (结果个数 = 1)
  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SHAPINGBUFUSED.md`
