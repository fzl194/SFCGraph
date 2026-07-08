# 查询全局Diameter域（LST UPGLBDIAMREALM）

- [命令功能](#ZH-CN_CONCEPT_0000206297314567__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206297314567__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206297314567__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206297314567__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206297314567__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000206297314567__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206297314567)

**适用NF：UPF**

该命令用于查询全局Diameter域。

#### [注意事项](#ZH-CN_CONCEPT_0000206297314567)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206297314567)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206297314567)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATION | Diameter应用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定全局Diameter域所属的Diameter应用。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：根据实际应用场景选择对应的枚举值。 |

#### [使用实例](#ZH-CN_CONCEPT_0000206297314567)

- 查询全局Diameter域与SWM应用的绑定关系：
  ```
  LST UPGLBDIAMREALM: APPLICATION=SWM;
  ```
  ```

  RETCODE = 0  操作成功
  全局Diameter域名
  ----------------
                    Diameter应用  =  SWM
     根据IMSI构造归属地Realm开关  =  不使能
                    Diameter域名  =  test.huawei.com
  (结果个数 = 1)
  ---    END
  ```
- 查询所有全局Diameter域的绑定关系：
  ```
  LST UPGLBDIAMREALM:;
  ```
  ```

  RETCODE = 0  操作成功
  全局Diameter域名
  ----------------
                    Diameter应用  =  SWM
     根据IMSI构造归属地Realm开关  =  不使能
                    Diameter域名  =  test.huawei.com
  (结果个数 = 1)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0000206297314567)

参见ADD UPGLBDIAMREALM的参数说明。
