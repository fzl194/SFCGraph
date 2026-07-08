# 查询NAT静态地址映射关系（DSP NATSTATICMAPPING）

- [命令功能](#ZH-CN_CONCEPT_0000201105939508__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201105939508__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201105939508__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201105939508__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201105939508__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000201105939508__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201105939508)

**适用NF：UPF**

该命令用于查询NAT静态地址映射关系。

#### [注意事项](#ZH-CN_CONCEPT_0000201105939508)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201105939508)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201105939508)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：查询类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INSIDEIPV4：私网IPv4地址。<br>- GLOBALIPV4：公网IPv4地址。<br>默认值：无<br>配置原则：无 |
| STATICMAPNAME | 静态地址映射关系名称 | 可选必选说明：必选参数<br>参数含义：静态地址映射关系名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| INSIDEIPV4 | 私网IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“INSIDEIPV4”时为必选参数。<br>参数含义：私网IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| GLOBALIPV4 | 公网IPv4地址 | 可选必选说明：可选参数<br>参数含义：公网IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PORT | 端口 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“GLOBALIPV4”时为必选参数。<br>参数含义：端口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000201105939508)

该命令用于查询NAT静态地址映射关系：

```
DSP NATSTATICMAPPING: QUERYTYPE=INSIDEIPV4, STATICMAPNAME="map1", INSIDEIPV4="10.2.2.8";
```

```

RETCODE = 0  Operation Success.

Static Mapping Information:
---------------------------
                  Static Mapping Name  =  map1
                  Inside IPv4 Address  =  10.2.2.8
                  Global IPv4 Address  =  10.x.x.x
Start Port of the Global IPv4 Address  =  2048
  End Port of the Global IPv4 Address  =  4095
(Number of results = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000201105939508)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 静态地址映射关系名称 | 静态地址映射关系名称。 |
| 私网IPv4地址 | 私网IPv4地址。 |
| 公网IPv4地址 | 公网IPv4地址。 |
| 公网IPv4地址起始端口 | 公网IPv4地址起始端口。 |
| 公网IPv4地址结束端口 | 公网IPv4地址结束端口。 |
