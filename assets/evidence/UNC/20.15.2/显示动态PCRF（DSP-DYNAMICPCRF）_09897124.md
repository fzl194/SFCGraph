# 显示动态PCRF（DSP DYNAMICPCRF）

- [命令功能](#ZH-CN_CONCEPT_0209897124__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897124__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897124__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897124__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897124__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897124__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897124)

**适用NF：PGW-C、GGSN**

该命令用来查询动态PCRF主机信息。

#### [注意事项](#ZH-CN_CONCEPT_0209897124)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897124)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897124)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | PCRF主机名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示动态PCRF主机的主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。<br>默认值：无<br>配置原则：<br>- 该参数使用DSP DYNAMICPCRF命令配置生成。<br>- 不输入此可选参数时，查询所有使用的动态PCRF。在了解对端PCRF的组网配置情况下，输入该参数，查询单个动态PCRF。 |

#### [使用实例](#ZH-CN_CONCEPT_0209897124)

- 查询名为dyn_pcrf的动态PCRF主机信息：
  ```
  DSP DYNAMICPCRF:HOSTNAME="dyn_pcrf";
  ```
  ```

  RETCODE = 0  Operation Success.

  Dynamic PCRF Information
  ------------------------
  PCRF Host Name  =  dyn_pcrf
      Realm Name  =  huawei
        POD Name  =  uncpod-0
  (Number of results = 1)
  ```
- 查询所有动态PCRF主机信息：
  ```
  DSP DYNAMICPCRF:;
  ```
  ```

  RETCODE = 0  Operation Success.

  Dynamic PCRF Information
  ------------------------
  PCRF Host Name    Realm Name    POD Name 
  dyn_pcrf          huawei        uncpod-0  
  new_pcrf          huawei        uncpod-0  
  (Number of results = 2)
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897124)

| 输出项名称 | 输出项解释 |
| --- | --- |
| PCRF主机名称 | 用于表示动态PCRF主机的主机名。 |
| 域名 | 用于表示动态PCRF主机的域名。 |
| POD名称 | 用于表示动态PCRF主机所在的POD资源单元。 |
