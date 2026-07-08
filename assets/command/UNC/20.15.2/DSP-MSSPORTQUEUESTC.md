---
id: UNC@20.15.2@MMLCommand@DSP MSSPORTQUEUESTC
type: MMLCommand
name: DSP MSSPORTQUEUESTC（显示端口队列统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSPORTQUEUESTC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
status: active
---

# DSP MSSPORTQUEUESTC（显示端口队列统计信息）

## 功能

该命令用于显示指定端口的MSS端口多队列统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划。<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无。<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划。<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无。<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务实例号。 |
| PORTID | 端口号 | 可选必选说明：必选参数。<br>参数含义：该参数用于表示端口号。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无。<br>配置原则：使用<br>**[DSP MSSPORTINFO](显示端口信息（DSP MSSPORTINFO）_92520022.md)**<br>命令获取端口号。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSSPORTQUEUESTC]] · 端口队列统计信息（MSSPORTQUEUESTC）

## 使用实例

显示类型为104的微服务csdb-pod-0172-16-2-45__103__0端口2的队列统计信息：

```
%%DSP MSSPORTQUEUESTC: CELLTYPE="104", CELLINSTANCE="csdb-pod-0172-16-2-45__103__0", PORTID=2;%%
RETCODE = 0  操作成功

结果如下:
---------
                  端口号  =  2
                  端口名  =  uio0
                  队列ID  =  0
      队列发送的报文个数  =  880333
        队列发送的字节数  =  932486814
      队列接收的报文个数  =  975093
        队列接收的字节数  =  961601058
队列接收中丢弃的报文个数  =  0
            发送队列深度  =  4294967295
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MSSPORTQUEUESTC.md`
