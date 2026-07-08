---
id: UDG@20.15.2@MMLCommand@DSP SECTIONUSAGE
type: MMLCommand
name: DSP SECTIONUSAGE（显示地址段使用情况）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SECTIONUSAGE
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
- 地址段使用情况
status: active
---

# DSP SECTIONUSAGE（显示地址段使用情况）

## 功能

**适用NF：PGW-U、UPF**

此命令用于显示地址段使用情况的信息。

## 注意事项

- 查询结果相对地址实际释放的时间有1-5秒的延迟。
- 该命令只支持本地地址池下的地址段使用情况查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：地址池名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79。<br>默认值：无<br>配置原则：该参数使用ADD POOL命令配置生成。 |
| SECTIONNUM | 地址段号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置Section的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无<br>配置原则：该参数使用ADD SECTION命令配置生成。 |

## 操作的配置对象

- [地址段使用情况（SECTIONUSAGE）](configobject/UDG/20.15.2/SECTIONUSAGE.md)

## 使用实例

查询地址池名称为pool1的地址池，地址段号为0的使用率信息：

```
DSP SECTIONUSAGE: POOLNAME="pool1", SECTIONNUM=0;
```

```

RETCODE = 0  操作成功

地址段使用情况
-------------------------------
                  地址池名称  =  pool1
                    地址段号  =  0
                等待释放IP数  =  0          
                    地址总数  =  10
                  地址使用数  =  0
                  地址无效数  =  0
                  锁定地址数  =  0
        地址使用数(锁定地址)  =  0
        地址使用数(冲突地址)  =  0
           地址段使用率（%）  =  0
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示地址段使用情况（DSP-SECTIONUSAGE）_20909913.md`
