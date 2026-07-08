# 显示Diameter Route状态（DSP DIAMRTSTATUS）

- [命令功能](#ZH-CN_CONCEPT_0209897308__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897308__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897308__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897308__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897308__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897308__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897308)

**适用NF：PGW-C、SMF**

此命令用来查询Diameter路由的状态。

#### [注意事项](#ZH-CN_CONCEPT_0209897308)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897308)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897308)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALM | Diameter域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter应用的域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| APPLICATION | Diameter应用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter协议中的应用类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GY：Gy接口应用。<br>- GX：Gx接口应用。<br>- S6B：S6b接口应用。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897308)

- 查询Diameter realm为"gx-realm"的Diameter Route信息：
  ```
  DSP DIAMRTSTATUS: REALM="gx-realm",APPLICATION=GX;
  ```
  ```

  RETCODE = 0  操作成功。

  Diameter路由状态
  ----------------
  Diameter域名    Diameter应用    POD名称   状态   
  gx-realm        Gx              uncpod-0  Normal 
  gx-realm        Gx              uncpod-0  Abnormal 
  (结果个数 = 2)
  ```
- 查询全部Diameter Route信息：
  ```
  DSP DIAMRTSTATUS:;
  ```
  ```

  RETCODE = 0  操作成功。

  Diameter路由状态
  ----------------
  Diameter域名    Diameter应用    POD名称   状态   
  gx-realm        Gx              uncpod-0  Normal 
  gy-realm        Gy              uncpod-0  Normal 
  gx-realm        Gx              uncpod-0  Abnormal 
  gy-realm        Gy              uncpod-0  Abnormal 
  (结果个数 = 4)
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897308)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Diameter域名 | 用于指定Diameter应用的域名。 |
| Diameter应用 | 用于指定Diameter协议中的应用类型。 |
| POD名称 | 用户指定查询到的Diameter Route所在的POD资源单元名称。 |
| 状态 | 用于指定查询到的Diameter Route的状态。 |
