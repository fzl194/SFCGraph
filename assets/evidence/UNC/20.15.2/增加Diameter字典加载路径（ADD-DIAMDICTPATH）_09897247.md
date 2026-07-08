# 增加Diameter字典加载路径（ADD DIAMDICTPATH）

- [命令功能](#ZH-CN_CONCEPT_0209897247__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897247__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897247__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897247__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897247__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897247)

**适用NF：PGW-C、SMF**

该命令用于增加Diameter字典加载路径。

#### [注意事项](#ZH-CN_CONCEPT_0209897247)

- 该命令执行后立即生效。
- 该命令最大记录数为5。
- 只有为某应用增加第二套字典加载路径时，才会使用该命令。
- 目前只支持GY应用设置第二套字典加载路径。
- 该命令执行后，再执行加载字典命令（LOD DIAMDICT）。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | APPLICATION | DICTNO | DICTPATH |
| --- | --- | --- | --- |
| 初始值 | GY | 1 | EPC_STANDARD |
| 初始值 | GX | 1 | EPC970_STANDARD |
| 初始值 | S6B | 1 | EPC_STANDARD |

#### [操作用户权限](#ZH-CN_CONCEPT_0209897247)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897247)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATION | 应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定字典的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GY：Gy接口字典。<br>- GX：Gx接口字典。<br>- S6B：S6b接口字典。<br>默认值：无<br>配置原则：无 |
| DICTNO | 字典序号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定字典编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2。<br>默认值：无<br>配置原则：无 |
| DICTPATH | 字典加载路径 | 可选必选说明：必选参数<br>参数含义：该参数用于指定字典加载路径。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- EPC_STANDARD：EPC标准字典路径。<br>- GU_STANDARD：GU标准字典路径。<br>- CUSTOM1：定制字典路径1。<br>- CUSTOM2：定制字典路径2。<br>- EPC970_STANDARD：EPC 970 标准字典路径。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897247)

当需要为GY应用增加第二套字典加载路径时：

```
ADD DIAMDICTPATH: APPLICATION=GY,DICTNO=2,DICTPATH=CUSTOM2;
```
