# 查询全局扩展策略（LST GLBEXTENDPOLICY）

- [命令功能](#ZH-CN_CONCEPT_0209678530__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209678530__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209678530__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209678530__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209678530__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209678530__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209678530)

**适用NF：PGW-U、UPF**

该命令用于显示对应扩展策略类型的全局扩展策略。

#### [注意事项](#ZH-CN_CONCEPT_0209678530)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209678530)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209678530)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXTENDPLYTYPE | 扩展策略类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TETHERING：表示在没有超规格的情况下对Tethering前后台进行控制。<br>- EXCEED_TETHERING：表示在超规格情况下对Tethering前后台进行控制。<br>默认值：无<br>配置原则：根据部署的业务策略选择相应的策略类型。 |

#### [使用实例](#ZH-CN_CONCEPT_0209678530)

假如运营商希望查看扩展策略类型为TETHERING的全局扩展策略：

```
LST GLBEXTENDPOLICY:;
```

```

RETCODE = 0 操作成功。

全局扩展策略配置
--------------------
扩展策略类型      业务属性名称       Tethering策略类型            策略名称

TETHERING           NULL                 TETHERING_HOTSPOT             cp01         
TETHERING           sp01                 TETHERING_TERMINAL            cp01         
(结果个数 = 2)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209678530)

参见ADD GLBEXTENDPOLICY的参数说明。
